
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():
	#Return version string.#
	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Setup for autopep import astfrom setuptools import setup
def version():
	#Return version string.#
	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Setup for autopep.import astfrom setuptools import setup
def version():
	#Return version string.#
	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()

   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()
import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()
   packages=['mailpile'],
   entry_points = {
	 'console_scripts': [
	   'mailpilemain'
	 ]
   },
)
# -*- coding: utf-8 -
#
# This file is part of offset. See the NOTICE for more information.
# copyright (c) 2013 David Reid under the MIT License.
from offset.sync.atomic import AtomicLong, ffi, libdef test_long_add_and_fetch():	assert lib.long_add_and_fetch(l, 1) == 1
	assert lib.long_add_and_fetch(l, 10) == 11def test_long_sub_and_fetch():	assert lib.long_sub_and_fetch(l, 1) == -1
	assert lib.long_sub_and_fetch(l, 10) == -11def test_long_bool_compare_and_swap():	assert lib.long_bool_compare_and_swap(l, 0, 10) == True
	assert lib.long_bool_compare_and_swap(l, 1, 20) == Falsedef test_atomiclong_repr():
	l = AtomicLong(123456789)
 def test_atomiclong_value():
	l = AtomicLong(0)
	assert l.value == 0
	l.value = 10
	assert l.value == 10def test_atomiclong_iadd():
	l = AtomicLong(0)
	l += 10
	assert l.value == 10def test_atomiclong_isub():
	l = AtomicLong(0)
	l -= 10
	assert l.value == -10def test_atomiclong_eq():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)
	assert l1 == 0
	assert l1 != 1
	assert not (l2 == 0)
	assert not (l2 != 1)
	assert l1 == l3
	assert not (l1 != l3)
	assert l1 != l2
	assert not (l1 == l2)def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()def test_atomiclong_ordering():
	l1 = AtomicLong(0)
	l2 = AtomicLong(1)
	l3 = AtomicLong(0)	assert l1 < l2
	assert l1 <= l2
	assert l1 <= l3
	assert l2 > l1
	assert l2 >= l3
	assert l2 >= l2	assert l1 < 1
	assert l1 <= 0
	assert l1 <= 1
	assert l1 > -1
	assert l1 >= -1
	assert l1 >= 0
#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

#!/usr/bin/python
from datetime import date
from setuptools import setup
from mailpile.app import APPVER
import ostry:

import unittest
import mailpileclass TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
class TestSearch(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_index(self):
	res = self.mp.rescan()
	self.assertEqual(res.as_dict()["result"], True)  def test_search(self):
	# A random search must return results in less than 0.2 seconds.
	res = self.mp.search("foo")
	self.assertLess(float(res.as_dict()["elapsed"]), 0.2)
class TestTagging(unittest.TestCase):
  def setUp(self):
	self.mp = mailpile.Mailpile()  def test_addtag(self):
	pass  unittest.main()#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]
# read long description
with open(os.path.join(os.path.dirname(file), 'README')) as f:
	long_description = f.read()DATA_FILES = [
		('offset', ["LICENSE",  "NOTICE", "README",
						"THANKS"])
		]
setup(name='offset',		description = 'collection of modules to build distributed and reliable concurrent systems',
		long_description = long_description,
		classifiers = CLASSIFIERS,
		license = 'BSD',		author = 'Benoit Chesneau',		packages=find_packages(),
		install_requires = REQUIREMENTS,
		setup_requires=REQUIREMENTS,
		tests_require=['pytest'],
		ext_modules=EXT_MODULES,
		data_files = DATA_FILES,
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import astfrom setuptools import setup
def version():	with open('autopep') as input_file:
		for line in input_file:
			if line.startswith('version'):
				return ast.parse(line).body[0].value.s
with open('README') as readme:
	setup(
		name='autopep',
		version=version(),
		description='A tool that automatically formats Python code to conform '		long_description=readme.read(),
		license='Expat License',
		author='Hideo Hattori',	   
		py_modules=['autopep'],
		zip_safe=False,	)
import os
import sysfrom setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommandclass PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True	def run_tests(self):
		import pytest
		errno = pytest.main(self.test_args)
		sys.exit(errno)py_version = sys.version_info[:2]REQUIREMENTS = ["cffi"]if not is_pypy:
	REQUIREMENTS.append("fibers")if py_version == (2, 7):
	REQUIREMENTS.append('futures')try:
	from offset.sync.atomic import ffi
except ImportError:
	EXT_MODULES=[]
else:
	EXT_MODULES=[ffi.verifier.get_extension()]s
