use std::fs::File;
use std::io::{self, BufReader, prelude::*};

// start at 50
// from 0 to 100
// going left removes
// going right adds
//      how many times AFTER turning
//      will it point to 0

fn main() -> io::Result<()> {
    let file = File::open("test_input.txt")?;
    let reader = BufReader::new(file);

    let mut num = 50;
    let mut res = 0;

    for line in reader.lines() {
        println!("{}", line?);
        let (prefix, suffix) = line?
            .split_once(if line.contains('L') { 'L' } else { 'R' })
            .unwrap_or((&line[..], ""));
        if (prefix == "L") {
            num -= suffix.parse::<i32>().unwrap();
            while (num < 0) {
                num = 99 - num;
            }
        } else {
            num += suffix.parse::<i32>().unwrap();
            while (num > 99) {
                num -= 99;
            }
        }
        if (num == 0) {
            res += 1;
        }
    }

    Ok(())
}
