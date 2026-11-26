fn balances(changes: &[i32]) -> Vec<i32> {
    changes.iter().scan(0, |state, &change| {
        *state += change;
        Some(*state)
    }).collect()
}
fn main() {
    let changes = vec![3, -1, 4, -2, 0, 2];
    for total in balances(&changes) { print!("{total} "); }
    assert_eq!(changes.len(), 6);
}
