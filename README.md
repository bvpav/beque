# Beque

Beque is a
[concatenative](https://www.concatenative.org/wiki/view/Concatenative%20language)
[double-ended queue-based](https://en.wikipedia.org/wiki/Double-ended_queue)
programming language, inspired by
[Deque](https://www.concatenative.org/wiki/view/Deque).

## Syntax

`.1` - pushes a 1 to the right of the deque
`1.` - pushes a 1 to the left of the deque
`.+` - adds the right two numbers of the deque
`+.` - adds the left two numbers of the deque

## Examples

```beque
3. .5 .2 -. .+ .print
```

Output:

```
4
```

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
