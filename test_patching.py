from instrumentation.module_loader import PatchingPathFinder

PatchingPathFinder().install()

from module_to_patch import hello

foo = hello()
print(foo)
