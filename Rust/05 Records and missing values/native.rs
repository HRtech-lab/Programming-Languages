use std::collections::BTreeMap;
fn main() {
    let rows = [("A", Some(3)), ("B", Some(8)), ("A", Some(5)),
                ("C", Some(2)), ("B", None)];
    let mut groups = BTreeMap::new();
    for (name, value) in rows {
        if let Some(x) = value {
            let group = groups.entry(name).or_insert((0, 0));
            group.0 += x;
            group.1 += 1;
        }
    }
    for (_, (total, count)) in groups {
        print!("{} ", f64::from(total) / f64::from(count));
    }
}
