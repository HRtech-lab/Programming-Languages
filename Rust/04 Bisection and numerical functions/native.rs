fn root(n: f64) -> Result<f64, &'static str> {
    if n < 0.0 { return Err("negative radicand"); }
    if n == 0.0 { return Ok(0.0); }
    let (mut lo, mut hi) = (0.0, 1.0_f64.max(n));
    for _ in 0..55 {
        let mid = (lo + hi) / 2.0;
        if mid * mid < n { lo = mid; } else { hi = mid; }
    }
    Ok((lo + hi) / 2.0)
}
fn main() {
    for n in [0.0, 0.5, 2.0, 10.0, 25.0] {
        print!("{} ", root(n).expect("fixture is nonnegative"));
    }
}
