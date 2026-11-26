fn main() {
    let celsius: [i32; 5] = [-10, 0, 10, 20, 30];
    for c in celsius {
        print!("{} ", f64::from(c) * 9.0 / 5.0 + 32.0);
    }
}
