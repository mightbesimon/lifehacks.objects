'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from dataclasses import dataclass
from unittest import TestCase, main
from lifehacks.objects import Clist


################################################################
#######                    dataclass                     #######
################################################################
@dataclass
class Point:
	x: int
	y: int

################################################################
#######                      tests                       #######
################################################################
class TestClistInit(TestCase):

	def test_init_none(self) -> None:
		cl1 = Clist()      # type:ignore
		cl2 = Clist(None)  # type:ignore
		self.assertEqual(cl1, [])
		self.assertEqual(cl2, [])

	def test_init_args(self) -> None:
		l = [1, 2]
		cl1 = Clist[int](1)
		cl2 = Clist[int](1, 2)
		cl3 = Clist[int](*l)
		self.assertEqual(cl1, [1])
		self.assertEqual(cl2, [1, 2])
		self.assertEqual(cl3, [1, 2])

	def test_init_iterables(self) -> None:
		l = [1, 2]
		cl1 = Clist[int](l)
		cl2 = Clist[int]([l])
		self.assertEqual(cl1, l)
		self.assertEqual(cl2, [l])

	def test_init_dict(self) -> None:
		cl = Clist({'one': 1, 'two': 2})
		self.assertEqual(cl, [('one', 1), ('two', 2)])


class TestClistSelfChaining(TestCase):

	def test_add(self) -> None:
		...

	def test_sort(self) -> None:
		...

	def test_remove(self) -> None:
		...

	def test_reverse(self) -> None:
		...


class TestClistChaining(TestCase):

	def test_clone(self) -> None:
		...

	def test_filter(self) -> None:
		...

	def test_map(self) -> None:
		...

	def test_flatten(self) -> None:
		...

	def test_unique(self) -> None:
		...

	def test_zip(self) -> None:
		...


class TestClistNonChaining(TestCase):

	def test_first(self) -> None:
		cl1 = Clist[int]()
		cl2 = Clist[int](1, 2)
		self.assertEqual(cl1.first(), None)
		self.assertEqual(cl1.first(0), 0)
		self.assertEqual(cl2.first(), 1)
		# self.assertEqual(cl2.first(lambda item: item>1), 2)
		self.assertEqual(cl2.first(lambda item: item>2, default=0), 0)

	def test_last(self) -> None:
		...

	def test_same(self) -> None:
		...

	def test_len(self) -> None:
		cl1 = Clist[int](0, 1, 2)
		self.assertEqual(cl1.len(), 3)

	def test_all(self) -> None:
		cl1 = Clist(False, True)
		cl2 = Clist(True , True)
		cl3 = Clist(0, 1, 2)
		self.assertFalse(cl1.all())
		self.assertTrue(cl2.all())
		self.assertFalse(cl3.all(lambda x: x%2==1))
		self.assertTrue(cl3.all(lambda x: x>0))

	def test_any(self) -> None:
		cl1 = Clist(False, False)
		cl2 = Clist(False, True )
		cl3 = Clist(0, 1, 2)
		self.assertFalse(cl1.any())
		self.assertTrue(cl2.any())
		self.assertTrue(cl3.any(lambda x: x%2==1))
		self.assertFalse(cl3.any(lambda x: x>2))

	def test_max(self) -> None:
		cl1 = Clist(1, 2, 3)
		cl2 = Clist(
			Point(1, 1),
			Point(2, 2),
			Point(3, 3),
		)
		self.assertEqual(cl1.max(), 3)
		self.assertEqual(cl2.max(lambda p: p.x), cl2[2])

	def test_min(self) -> None:
		cl1 = Clist(1, 2, 3)
		cl2 = Clist(
			Point(1, 1),
			Point(2, 2),
			Point(3, 3),
		)
		self.assertEqual(cl1.min(), 1)
		self.assertEqual(cl2.min(lambda p: p.x), cl2[0])

	def test_sum(self) -> None:
		cl1 = Clist(1, 2, 3)
		self.assertEqual(cl1.sum(), 6)

	def test_str(self) -> None:
		cl1 = Clist(1, 2, 3)
		self.assertEqual(cl1.str(), '[1, 2, 3]')

	def test_dict(self) -> None:
		cl1 = Clist((1, 10), (2, 20), (3, 30))
		cl2 = Clist(1, 2, 3)
		self.assertEqual(cl1.dict(), {1: 10, 2: 20, 3: 30})
		self.assertRaises(TypeError, cl2.dict)

	def test_tuple(self) -> None:
		cl1 = Clist(1, 2, 3)
		self.assertEqual(cl1.tuple(), (1, 2, 3))

	def test_set(self) -> None:
		cl1 = Clist(1, 2, 3)
		self.assertEqual(cl1.set(), {1, 2, 3})


class TestClistDunderMethods(TestCase):

	def test_repr(self) -> None:
		cl1 = Clist[int](0, 1, 2)
		self.assertEqual(repr(cl1), '[0, 1, 2]')

	def test_str(self) -> None:
		cl1 = Clist[int](0, 1, 2)
		self.assertEqual(str(cl1), '[0, 1, 2]')

	def test_len(self) -> None:
		cl1 = Clist[int](0, 1, 2)
		self.assertEqual(len(cl1), 3)

	def test_iter(self) -> None:
		cl1 = Clist[int](0, 1, 2)
		self.assertEqual([item for item in cl1], [0, 1, 2])

	def test_getitem(self) -> None:
		cl1 = Clist[int](0, 1, 2)
		self.assertEqual(cl1[1], 1)
		self.assertEqual(cl1[1:], [1, 2])
		self.assertIsInstance(cl1[1:], Clist)

	def test_setitem(self) -> None:
		cl1 = Clist[int](0, 1, 2)
		cl1[0] = 3
		self.assertEqual(cl1, [3, 1, 2])
		cl1[1:] = [4, 5]
		self.assertEqual(cl1, [3, 4, 5])

	def test_delitem(self) -> None:
		cl1 = Clist[int](0, 1, 2)
		del cl1[0]
		self.assertEqual(cl1, [1, 2])
		del cl1[1:]
		self.assertEqual(cl1, [1])

	def test_add(self) -> None:
		cl1 = Clist[int](0, 1) + [2]
		self.assertEqual(cl1, [0, 1, 2])
		self.assertIsInstance(cl1, Clist)

	def test_iadd(self) -> None:
		cl1 = Clist[int](0, 1)
		cl1 += [2]
		self.assertEqual(cl1, [0, 1, 2])
		self.assertIsInstance(cl1, Clist)

	def test_mul(self) -> None:
		cl1 = Clist[int](0, 1) * 2
		self.assertEqual(cl1, [0, 1, 0, 1])
		self.assertIsInstance(cl1, Clist)

	def test_rmul(self) -> None:
		cl1 = 2 * Clist[int](0, 1)
		self.assertEqual(cl1, [0, 1, 0, 1])
		self.assertIsInstance(cl1, Clist)

	def test_imul(self) -> None:
		cl1 = Clist[int](0, 1)
		cl1 *= 2
		self.assertEqual(cl1, [0, 1, 0, 1])
		self.assertIsInstance(cl1, Clist)

	def test_contains(self) -> None:
		cl1 = Clist[int](0, 1, 2)
		self.assertTrue(1 in cl1)
		self.assertIn(1, cl1)

	def test_eq(self) -> None:
		cl1 = Clist[int](0, 1)
		self.assertEqual(cl1, Clist(0, 1))
		self.assertNotEqual(cl1, Clist(1))
		self.assertEqual(cl1, [0, 1])
		self.assertNotEqual(cl1, [1])
		self.assertNotEqual(cl1, 1)
		self.assertTrue (cl1==[0, 1])
		self.assertIsInstance(cl1, Clist)
		#todo

	def test_gt(self) -> None:
		...

	def test_ge(self) -> None:
		...

	def test_lt(self) -> None:
		...

	def test_le(self) -> None:
		...


################################################################
#######                 MAIN STARTS HERE                 #######
################################################################
if __name__ == '__main__':
	main()
