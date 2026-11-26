fn means(values: &[i32], width: usize) -> impl Iterator<Item = f64> + '_ {
    assert!(width > 0);
    values.windows(width).map(|window| {
        f64::from(window.iter().sum::<i32>()) / window.len() as f64
    })
}
fn main() {
    let readings = vec![2, 4, 8, 1, 3, 7];
    for mean in means(&readings, 3) { print!("{mean} "); }
}
