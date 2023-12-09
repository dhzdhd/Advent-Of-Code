import gleam/io
import simplifile.{read}
import gleam/string
import gleam/list

pub fn is_ap(xs: List(Int)) -> Bool {
  todo
}

pub fn main() {
  let assert Ok(raw) = read(from: "./input.txt")
  io.println("content")

  let contents = list.window_by_2
}
