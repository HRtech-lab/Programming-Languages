changes <- c(3, -1, 4, -2, 0, 2)
balances <- cumsum(changes)
stopifnot(tail(balances, 1) == sum(changes))
cat(balances)
