#!/usr/bin/env python3
from typing import Optional, List, TextIO, Iterable
from sys import argv, stdin, exit, stdout
from pathlib import Path
import logging

import click


NAME = Path(argv[0]).name

LOWEST = 0
RC_NO_ARGS = 1

READ_BYTES = 'rb'
NEW_LINE = b'\n'


def gen_lines_end(line_nums: List[int], content: TextIO=stdin) -> Iterable[str]:
    pass


def gen_lines(
    line_nums: List[int],
    content: TextIO=stdin
) -> Iterable[str]:
  line_nums = sorted(line_nums)
  # line: int = None

  for nth, line in enumerate(content):
    if nth == line_nums[LOWEST]:
      yield line
      del line_nums[LOWEST]

      if not line_nums:
        break

  # if line_nums and line:
    # yield line


def exclude_lines(
    line_nums: List[int],
    content: TextIO=stdin
) -> Iterable[str]:
  line_nums = set(line_nums)

  for nth, line in enumerate(content):
    if nth not in line_nums:
      yield line

    else:
      line_nums.remove(nth)


@click.command(help=f"""Return the contents of stdin from the line numbers supplied as arguments.

Example:

  $ echo -e 'hello\\nworld\\n!'| {NAME} 1

  world
""")
@click.argument('lines', nargs=-1, type=click.INT)
@click.option('-r', '--reverse', is_flag=True, 
    help=f"Write every line, except the line numbers supplied as LINES, from stdin to stdout.")
@click.option('-f', '--file', type=click.File('r', lazy=True), default=None,
    help=f"Read from file instead of stdin.")
@click.option('-e', '--empty', is_flag=True, default=False
    help=f"Do not filter out blank lines, or lines consisting only of whitespace, from output.")
def cmd(lines: List[str], reverse: bool, file: TextIO, empty: bool):
  if not lines and not reverse:
    logging.error(f"No line numbers specified as arguments to {NAME}.")
    exit(RC_NO_ARGS)

  content = file if file else stdin.fileno()
  line_gen_func = exclude_lines if reverse else gen_lines

  with open(input, READ_BYTES) as content:
    output_lines = line_gen_func(lines, content)

    for line in output_lines:
      if line or empty:  # filter out empty lines
        stdout.buffer.write(line)


if __name__ == "__main__":
  cmd()
