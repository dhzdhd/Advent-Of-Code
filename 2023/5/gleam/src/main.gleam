import gleam/io
import simplifile.{read}
import gleam/string
import gleam/list

pub fn main() {
  let assert Ok(raw) = read(from: "./input.txt")
  io.println("content")

  let contents =
    raw
    |> string.split(on: "\r\n\r\n")

  contents
  |> list.map(fn(str) { io.debug(str) })
}
