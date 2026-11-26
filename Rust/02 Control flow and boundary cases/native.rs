fn main() {
    let mut counts = [0_u32; 3];
    for value in [-4, 0, 5, 12, 18, 25, 31] {
        let class = match value { ..=0 => 0, 1..=19 => 1, _ => 2 };
        counts[class] += 1;
    }
    for n in counts { print!("{n} "); }
}
