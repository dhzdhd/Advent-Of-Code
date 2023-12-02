import gleam/io
import simplifile.{FileError, read}

pub fn main() {
  let assert raw = read(from: "./input.txt")
  io.println("content")
}
