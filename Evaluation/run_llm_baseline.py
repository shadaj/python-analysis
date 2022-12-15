import os
import openai
import time

from absl import app
from absl import flags

flags.DEFINE_enum('model', None, ['code-cushman-001', 'code-davinci-002'], 'Which model to use for evaluation')
flags.DEFINE_enum('dataset', None, ['1', '2', '3'], 'Which dataset to evaluate on (1: Codex generated codes, 2: Variable Masking on (1), 3: Dead Code Insertion and Function Reordering on (2))')
flags.mark_flags_as_required(['model', 'dataset'])
FLAGS = flags.FLAGS


def main(_):
  global FLAGS

  filedir = os.path.dirname(os.path.realpath(__file__))
  os.chdir(filedir)
  openai.api_key = os.getenv("OPENAI_API_KEY")
  path = os.path.join('Datasets', 'Wild-baseline-' + FLAGS.dataset)
  model =  FLAGS.model
  files = [i for i in os.listdir(os.path.join(path)) if i[-3:] == ".py" and i != "test.py"]

  print("#######################################################")
  print("Evaluating Wild dataset %s on model %s"%(FLAGS.dataset, model))
  print("#######################################################")

  correct1 = 0
  correct2 = 0
  correct3 = 0
  total = 0

  for i, filename in enumerate(files):
    file = os.path.join(path, filename)
    fp = open(file)
    file_content = fp.readlines()
    file_content = ''.join(file_content)

    question = """
      
    #Recommend a NumPy API which is equivalent to func.
    import numpy as np
    #The numpy API is np."""

    prompt = file_content + question
    retry = True
    print_response = True
    while retry:
      try:
        response = openai.Completion.create(
          model=model,
          prompt=prompt,
          temperature=0.1,
          max_tokens=50,
          top_p=1.0,
          n=3,
          frequency_penalty=0.0,
          presence_penalty=0.0,
          stop=["#", ";", "\n"]
        )
        retry = False
      except openai.error.InvalidRequestError:
        print(filename)
        print("Model cannot handle")
        retry = False
        print_response = False
      except:
        timeout = 30
        print("Exceeding rate limit, sleeping for %d sec"%timeout)
        time.sleep(timeout)
        retry = True

    ind = filename.index('-')
    label = filename[:ind] 
    if print_response:
      print("API ", i, ":")
      print(label)
      guess1 = response["choices"][0]["text"]
      guess2 = response["choices"][1]["text"]
      guess3 = response["choices"][2]["text"]
      print("Pred 1: ", guess1)
      print("Pred 2: ", guess2)
      print("Pred 3: ", guess3)
      total += 1
      if label in guess1:
        correct1 += 1
        correct2 += 1
        correct3 += 1
      elif label in guess2:
        correct2 += 1
        correct3 += 1
      elif label in guess3:
        correct3 += 1

    print("###")

  print("Top 1 Correct: ", correct1, " Total: ", total, " Accuracy: ", correct1 / total)
  print("Top 2 Correct: ", correct2, " Total: ", total, " Accuracy: ", correct2 / total)
  print("Top 3 Correct: ", correct3, " Total: ", total, " Accuracy: ", correct3 / total)

if __name__ == '__main__':
  app.run(main)
  