#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2013 The PyVFS Project Authors.
# Please see the AUTHORS file for details on individual authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The tar file system implementation."""

import tarfile

# This is necessary to prevent a circular import.
import pyvfs.vfs.tar_file_entry

from pyvfs.path import tar_path_spec
from pyvfs.vfs import file_system


class TarFileSystem(file_system.FileSystem):
  """Class that implements a file system object using tarfile."""

  LOCATION_ROOT = u'/'

  def __init__(self, file_object, path_spec, encoding='utf-8'):
    """Initializes the file system object.

    Args:
      file_object: the file-like object (instance of io.FileIO).
      path_spec: the path specification (instance of path.PathSpec) of
                 the file-like object.
      encoding: optional file entry name encoding. The default is 'utf-8'.
    """
    super(TarFileSystem, self).__init__()
    self._file_object = file_object
    self._path_spec = path_spec
    self.encoding = encoding

    # Explicitly tell tarfile not to use compression. Compression should be
    # handled by the file-like object.
    self._tar_file = tarfile.open(mode='r:', fileobj=file_object)

  def FileEntryExistsByPathSpec(self, path_spec):
    """Determines if a file entry for a path specification exists.

    Args:
      path_spec: a path specification (instance of path.PathSpec).

    Returns:
      Boolean indicating if the file entry exists.
    """
    tar_info = None
    location = getattr(path_spec, 'location', None)

    if (location is None or
        not location.startswith(self.LOCATION_ROOT)):
      return

    if len(location) == 1:
      return True

    try:
      tar_info = self._tar_file.getmember(location[1:])
    except KeyError:
      pass

    return tar_info is not None

  def GetFileEntryByPathSpec(self, path_spec):
    """Retrieves a file entry for a path specification.

    Args:
      path_spec: a path specification (instance of path.PathSpec).

    Returns:
      A file entry (instance of vfs.TarFileEntry) or None.
    """
    tar_info = None
    location = getattr(path_spec, 'location', None)

    if (location is None or
        not location.startswith(self.LOCATION_ROOT)):
      return

    if len(location) == 1:
      return self.GetRootFileEntry()

    try:
      tar_info = self._tar_file.getmember(location[1:])
    except KeyError:
      pass

    if tar_info is None:
      return
    return pyvfs.vfs.tar_file_entry.TarFileEntry(
        self, path_spec, tar_info=tar_info)

  def GetRootFileEntry(self):
    """Retrieves the root file entry.

    Returns:
      A file entry (instance of vfs.FileEntry).
    """
    path_spec = tar_path_spec.TarPathSpec(
        location=self.LOCATION_ROOT, parent=self._path_spec)

    return pyvfs.vfs.tar_file_entry.TarFileEntry(self, path_spec)

  def GetTarFile(self):
    """Retrieves the tar file object.

    Returns:
      The tar file object (instance of tarfile.TarFile).
    """
    return self._tar_file