#!/usr/bin/env python3
from typing import Optional, List, TextIO, Iterable
from sys import argv, stdin, exit, stdout
from pathlib import Path

import click


NAME = Path(argv[0]).name

LOWEST = 0
RC_NO_ARGS = 1

READ_BYTES = 'rb'
NEW_LINE = b'\n'

def gen_lines_end(lines: List[int], input: TextIO=stdin) -> Iterable[str]:
    pass

def gen_lines(lines: List[int],
              content: TextIO=stdin) -> Iterable[str]:
  lines = sorted(lines)
  line: int = None

  for nth, line in enumerate(content):
    if nth == lines[LOWEST]:
      yield line
      del lines[LOWEST]

      if not lines:
        break

  #if lines and line:
    #yield line


def exclude_lines(lines: List[int],
                  content: TextIO=stdin) -> Iterable[str]:
  lines = set(lines)

  for nth, line in enumerate(content):
    if nth not in lines:
      yield line

    else:
      lines.remove(nth)


@click.command(help=f"""Return the contents of stdin from the line numbers supplied as arguments.

Example:

  $ echo -e 'hello\\nworld\\n!'| {NAME} 1

  world
""")
@click.argument('lines', nargs=-1, type=click.INT)
@click.option('-r', '--reverse', is_flag=True, help=f"Write every line, except the line numbers supplied as LINES, from stdin to stdout.")
@click.option('-f', '--file', help=f"Read from file instead of stdin.", type=click.File('r', lazy=True), default=None)
@click.option('-e', '--empty', is_flag=True, help=f"Do not filter out blank lines, or lines consisting only of whitespace, from output.", default=False)
def cmd(lines: List[str], reverse: bool, file: TextIO, empty: bool):
  if not lines and not reverse:
    print(f"No line numbers specified as arguments to {NAME}.")
    exit(RC_NO_ARGS)

  input = file if file else stdin.fileno()

  with open(input, READ_BYTES) as input:
    output = (exclude_lines if reverse else gen_lines)(lines, input)

    for line in output:
      if line or empty:  # filter out empty lines
        stdout.buffer.write(line)


if __name__ == "__main__":
  cmd()
