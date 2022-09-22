'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from typing import Any, Callable, Generic, Iterable, Iterator, TypeVar


T = TypeVar('T')
Self = TypeVar('Self')

################################################################
#######                      class                       #######
################################################################
class Clist(Generic[T], Iterable):
	'''	chaining list\n
		provide LINQ like methods for data storing lists
		```python
		```
	'''
	def __init__(self, *args:T|Iterable|dict|None|Ellipsis) -> None:
		'''	returns `self` to allow chaining queries
			```python
			mydata = ( Clist(item1, item2)
				.add(item3)
				.add(item4, item5)
			)	# [item1, item2, item3, item4, item5]
			```
		'''
		self.items:list[T] = []

		if len(args)==1 and (args[0] is None or args[0] is ...):
			return

		if len(args)==1 and isinstance(args[0], dict):
			self.items = [ (key, value)
				for key, value in args[0].items()
			]
			return

		if len(args)==1 and isinstance(args[0], Iterable):
			self.items = list(args[0])
			return

		self.items = list(args)

######################   self-chaining   #######################

	def add(self, *items:T) -> Clist[T]:
		'''	returns `self` to allow chaining queries
			```python
			mydata = ( Clist[int](1, 2)
				.add(3)
				.add(4, 5)
			)	# [1, 2, 3, 4, 5]
			```
		'''
		self.items.extend(items)
		return self

	def sort(self, *, key:Callable=..., reverse:bool=False) -> Clist[T]:
		'''	returns `self`to allow chaining queries\n
			```python
			mydata = ( Clist[int](1, 2, 3)
				.sort(reverse=True)
			)	# [3, 2, 1]
			```
		'''
		self.items.sort(key, reverse)
		return self

	def remove(self, item:T) -> Clist[T]:
		'''	returns `self`to allow chaining queries\n
			also, same to remove non-existing items \n
			```python
			mydata = ( Clist[int](1, 2, 3)
				.remove(0)
				.remove(2)
			)	# [1, 3]
			```
		'''
		if item in self:
			self.items.remove(item)
		return self

	def reverse(self) -> Clist[T]:
		...

#########################   chaining   #########################

	def clone(self) -> Clist[T]:
		return ... #todo

	def filter(self,
		function:Callable[[T], bool]=None,
		**kwargs:Any
	) -> Clist[T]:
		'''	returns a Clist to allow chaining queries
		'''
		# if no specified function, use kwargs for matches #todo
		if function is None: # todo
			function = lambda item: all(
				getattr(item, attribute)==value
				for attribute, value in kwargs.items()
			)

		# returns an Clist to allow chaining queries
		return Clist(
			filter(function, self)
		)

	def map(self, function:Callable[[T], Any]) -> Clist[Any]:
		'''	returns a Clist to allow chaining queries
		'''
		return Clist(
			map(function, self)
		)

	def flatten(self) -> Clist[Clist]:
		'''	flatten from 2D list to 1D list
		'''
		return Clist( subitem
			for item in self
			for subitem in item
		)

	def unique(self) -> Clist[T]:
		'''	preserves order
		'''
		# `Clist(set(self))` doesn't preserve order
		return Clist(dict.fromkeys(self))

	def zip():...

#######################   non-chaining   #######################

	def first(self,
		default:T=None,
		function:Callable[[T], bool]=None,
		**kwargs:Any
	) -> T:
		'''
		'''
		return (
			self.filter(function, **kwargs)[0]
			if self.len() else default
		)

	def last(self,
		default:T=None,
		function:Callable[[T], bool]=None,
		**kwargs:Any
	) -> T:
		'''
		'''
		return (
			self.filter(function, **kwargs)[-1]
			if self.len() else default
		)

	def len(self) -> int:
		'''	```python
			mydata = Clist(item1, item2)
			mydata.length() # 2
			```
		'''
		return len(self)

	def all(self,
		function:Callable[[T], bool]=None,
		**kwargs:Any
	) -> bool:
		'''
		'''
		# todo
		return self.len()==len(
			self.filter(function=function, **kwargs)
		)

	def any(self,
		function:Callable[[T], bool]=None,
		**kwargs:Any
	) -> bool:
		'''
		'''
		if function is None:
			function = lambda item: item

		return any(self.map(function=function))

	def max(self) -> T:
		...

	def min(self) -> T:
		...

	def sum(self) -> T:
		...

	def str(self) -> str:
		return str(self)

	def dict(self) -> dict:
		return { key: value for key, value in self } # todo

	def tuple(self) -> tuple:
		...

	def set(self) -> set:
		...

######################   dunder methods   ######################

	def __repr__(self) -> str:
		return self.items.__repr__()

	def __str__(self) -> str:
		return self.items.__str__()


	def __len__(self) -> int:
		return self.items.__len__()

	def __iter__(self) -> Iterator[T]:
		return self.items.__iter__()


	def __getitem__(self, idx:int|slice) -> T|list[T]:
		return self.items.__getitem__(idx) #todo cast type

	def __setitem__(self, idx:int|slice, obj:T|Iterable[T]) -> None:
		self.items.__setitem(idx, obj)

	def __delitem__(self, idx:int|slice) -> None:
		self.items.__delitem__(idx)


	def __add__(self, other:Iterable[T]) -> Clist[T]:
		return Clist(self.items.__add__(list(other)))

	def __iadd__(self, other:Iterable[T]) -> None:
		self.items.__iadd__(other)

	def __mul__(self, num:int) -> Clist[T]:
		return Clist(self.items.__mul__(num))

	def __rmul__(self, num:int) -> Clist[T]:
		return Clist(self.items.__rmul__(num))

	def __imul__(self, num:int) -> None:
		self.items.__imul__(num)


	def __contains__(self, item:T) -> bool:
		return self.items.__contains__(item)

	def __eq__(self, other:Iterable[T]) -> bool:
		return self.items.__eq__(list(other))

	def __gt__(self, other:Iterable[T]) -> bool:
		return self.items.__gt__(list(other))

	def __ge__(self, other:Iterable[T]) -> bool:
		return self.items.__ge__(list(other))

	def __lt__(self, other:Iterable[T]) -> bool:
		return self.items.__lt__(list(other))

	def __le__(self, other:Iterable[T]) -> bool:
		return self.items.__le__(list(other))
