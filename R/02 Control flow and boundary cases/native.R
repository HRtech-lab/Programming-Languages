x <- c(-4, 0, 5, 12, 18, 25, 31)
group <- ifelse(x <= 0, "low", ifelse(x < 20, "middle", "high"))
ordered_groups <- factor(group, levels = c("low", "middle", "high"))
cat(as.integer(table(ordered_groups)))
