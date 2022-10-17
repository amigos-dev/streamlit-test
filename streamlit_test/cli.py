# Copyright (c) 2022 Amigos Development, Inc.
#
# MIT License - See LICENSE file accompanying this package.
#

"""Command-line interface"""

from typing import Optional, Sequence
import sys

def run(argv: Optional[Sequence[str]]=None) -> int:
  """Run the command-line tool with provided arguments

  Args:
      argv (Optional[Sequence[str]], optional):
          A list of commandline arguments (NOT including the program as argv[0]!),
          or None to use sys.argv[1:]. Defaults to None.

  Returns:
      int: The exit code that would be returned if this were run as a standalone command.
  """
  return 0
