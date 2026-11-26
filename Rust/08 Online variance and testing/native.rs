#[derive(Default)]
struct Moments { count: u32, mean: f64, m2: f64 }
impl Moments {
    fn update(&mut self, value: f64) -> f64 {
        self.count += 1;
        let delta = value - self.mean;
        self.mean += delta / f64::from(self.count);
        self.m2 += delta * (value - self.mean);
        self.m2 / f64::from(self.count)
    }
}
fn main() {
    let mut state = Moments::default();
    for x in [1, 2, 4, 5] { print!("{} ", state.update(1e9 + f64::from(x))); }
}
