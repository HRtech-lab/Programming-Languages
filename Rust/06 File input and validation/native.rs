use std::{error::Error, fs};
fn main() -> Result<(), Box<dyn Error>> {
    let text = fs::read_to_string("readings.csv")?;
    let mut values = Vec::new();
    let mut rejected = 0;
    for line in text.lines().skip(1) {
        match line.trim().parse::<i32>() {
            Ok(value) => values.push(value),
            Err(_) => rejected += 1,
        }
    }
    let minimum = values.iter().min().ok_or("no numeric rows")?;
    let maximum = values.iter().max().ok_or("no numeric rows")?;
    print!("{} {} {minimum} {maximum} {rejected}", values.len(), values.iter().sum::<i32>());
    Ok(())
}
