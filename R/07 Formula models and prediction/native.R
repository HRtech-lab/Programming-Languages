train <- data.frame(x = 0:4, y = c(2, 5, 8, 11, 14))
model <- lm(y ~ x, data = train)
test <- data.frame(x = c(-1, 0, 2, 5))
cat(as.numeric(predict(model, newdata = test)))
