# -*- coding: utf-8 -*-
"""The VMDK image path specification implementation."""

from dfvfs.lib import definitions
from dfvfs.path import factory
from dfvfs.path import path_spec


class VMDKPathSpec(path_spec.PathSpec):
  """Class that implements the VMDK image path specification."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_VMDK

  def __init__(self, parent=None, **kwargs):
    """Initializes the path specification object.

    Note that the VMDK file path specification must have a parent.

    Args:
      parent: optional parent path specification (instance of PathSpec).
      kwargs: a dictionary of keyword arguments dependending on the path
              specification

    Raises:
      ValueError: when parent is not set.
    """
    if not parent:
      raise ValueError(u'Missing parent value.')

    super(VMDKPathSpec, self).__init__(parent=parent, **kwargs)

  @property
  def comparable(self):
    """Comparable representation of the path specification."""
    return self._GetComparable()


# Register the path specification with the factory.
factory.Factory.RegisterPathSpec(VMDKPathSpec)
