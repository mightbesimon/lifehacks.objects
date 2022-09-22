'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from typing import Any, Callable, Generic, Iterable, Iterator, TypeVar


T = TypeVar('T')
Tout = TypeVar('Tout')


class Clist(Generic[T], Iterable):
	'''
	'''
	def __init__(self, *args:T|Iterable|dict|None|Ellipsis) -> None:
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
		self.items.extend(items)
		return self

	def sort(self, *,
		key:Callable[[T], bool]=None,
		reverse:bool=False,
	) -> Clist[T]:
		self.items.sort(key, reverse)
		return self

	def remove(self, item:T) -> Clist[T]:
		if item in self: self.items.remove(item)
		return self

	def reverse(self) -> Clist[T]:
		self.items = self.items[::-1]
		return self

#########################   chaining   #########################

	def clone(self) -> Clist[T]:
		return ... #todo

	def filter(self,
		function:Callable[[T], bool]=None,
		**kwargs:Any,
	) -> Clist[T]:
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

	def map(self, function:Callable[[T], Tout]) -> Clist[Tout]:
		return Clist(
			map(function, self)
		)

	def flatten(self) -> Clist[Any]:
		return Clist( subitem
			for item in self
			for subitem in item
		)

	def unique(self) -> Clist[T]:
		# `Clist(set(self))` doesn't preserve order
		return Clist(dict.fromkeys(self).keys())

	def zip(self, *others:Iterable) -> Clist[T]:
		...

#######################   non-chaining   #######################

	def first(self,
		function:Callable[[T], bool]=None,
		default:T=None,
		**kwargs:Any,
	) -> T:
		return (
			self.filter(function, **kwargs)[0]
			if self.len() else default
		)

	def last(self,
		function:Callable[[T], bool]=None,
		default:T=None,
		**kwargs:Any,
	) -> T:
		return (
			self.filter(function, **kwargs)[-1]
			if self.len() else default
		)

	def same(self) -> bool:
		'''check if all items are equal'''
		return self.unique().len == 1

	def count(self,
		function:Callable[[T], bool]=None,
		**kwargs:Any,
	) -> int:
		return len(self)

	def len(self) -> int:
		return self.count()

	def all(self,
		function:Callable[[T], bool]=None,
		**kwargs:Any,
	) -> bool:
		# todo
		# wait why not all
		return self.len()==(self
			.filter(function=function, **kwargs)
			.len()
		)

	def any(self,
		function:Callable[[T], bool]=None,
		**kwargs:Any,
	) -> bool:
		return (self.filter(function=function, **kwargs).len()) > 0
		# todo kwargs
		# if function is None:
		# 	function = lambda item: item

		# return any(self.map(function=function))

	def max(self,
		key:Callable[[T], Any]=None,
	) -> T:
		return max(self.items, key=key)

	def min(self,
		key:Callable[[T], Any]=None,
	) -> T:
		return min(self, key=key)

	def sum(self) -> T:
		# todo map
		return sum(self)

	def str(self) -> str:
		return str(self)

	def dict(self) -> dict:
		return { key: value for key, value in self } # todo

	def tuple(self) -> tuple:
		return tuple(self)

	def set(self) -> set:
		return set(self)

######################   dunder methods   ######################

	def __repr__(self) -> str:
		return self.items.__repr__()

	def __str__(self) -> str:
		return self.items.__str__()

	def __len__(self) -> int:
		return self.items.__len__()

	def __iter__(self) -> Iterator[T]:
		return self.items.__iter__()

	def __getitem__(self, idx:int|slice) -> T|Clist[T]:
		result =  self.items.__getitem__(idx)
		return result if isinstance(idx, int) else Clist(result)

	def __setitem__(self, idx:int|slice, obj:T|Iterable[T]) -> None:
		self.items.__setitem__(idx, obj)

	def __delitem__(self, idx:int|slice) -> None:
		self.items.__delitem__(idx)

	def __add__(self, other:Iterable[T]) -> Clist[T]:
		return Clist(self.items.__add__(list(other)))

	def __iadd__(self, other:Iterable[T]) -> Clist[T]:
		self.items.__iadd__(other)
		return self

	def __mul__(self, num:int) -> Clist[T]:
		return Clist(self.items.__mul__(num))

	def __rmul__(self, num:int) -> Clist[T]:
		return Clist(self.items.__rmul__(num))

	def __imul__(self, num:int) -> Clist[T]:
		self.items.__imul__(num)
		return self

	def __contains__(self, item:T) -> bool:
		return self.items.__contains__(item)

	def __eq__(self, other:Iterable[T]) -> bool:
		return (
			self.items.__eq__(list(other))
			if isinstance(other, Iterable) else False
		)

	def __gt__(self, other:Iterable[T]) -> bool:
		return self.items.__gt__(list(other))

	def __ge__(self, other:Iterable[T]) -> bool:
		return self.items.__ge__(list(other))

	def __lt__(self, other:Iterable[T]) -> bool:
		return self.items.__lt__(list(other))

	def __le__(self, other:Iterable[T]) -> bool:
		return self.items.__le__(list(other))
