root <- function(n) {
  stopifnot(length(n) == 1L, is.finite(n), n >= 0)
  if (n == 0) return(0)
  lo <- 0
  hi <- max(1, n)
  for (i in seq_len(55L)) {
    mid <- (lo + hi) / 2
    if (mid * mid < n) lo <- mid else hi <- mid
  }
  (lo + hi) / 2
}
cat(sprintf("%.10f", vapply(c(0, 0.5, 2, 10, 25), root, numeric(1))))
