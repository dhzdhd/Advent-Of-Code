import gleam/io
import simplifile.{read}

pub fn main() {
  let assert Ok(raw) = read(from: "./input.txt")
  io.println("content")
}
