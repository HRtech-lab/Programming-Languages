d <- data.frame(id = c("A", "B", "A", "C", "B"),
                value = c(3, 8, 5, 2, NA_real_))
groups <- split(d$value, d$id)
avg <- vapply(groups, mean, numeric(1), na.rm = TRUE)
cat(avg[order(names(avg))])
