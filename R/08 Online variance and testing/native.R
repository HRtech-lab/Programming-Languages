count <- 0
centre <- 0
m2 <- 0
for (value in 1e9 + c(1, 2, 4, 5)) {
  count <- count + 1
  delta <- value - centre
  centre <- centre + delta / count
  m2 <- m2 + delta * (value - centre)
  cat(sprintf("%.10f ", m2 / count))
}
