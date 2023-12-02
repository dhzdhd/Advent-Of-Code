import gleam/io
import gleam/string.{contains}
import simplifile.{FileError, read}

pub fn main() {
  let raw = case read(from: "../../input.txt") {
    Ok(content) -> content
    Error(e) -> {
      // io.println(to_string(e))

      panic
    }
  }

  io.println(raw)
  io.println("Hello from main!")
}
