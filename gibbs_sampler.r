# Taken from slide 9 of http://www.stat.wisc.edu/~bates/JuliaForRProgrammers.pdf
Rgibbs <- function(N,thin) {
  mat <- matrix(0,nrow=N,ncol=2)
  x <- y <- 0
  for (i in 1:N) {
    for (j in 1:thin) {
      x <- rgamma(1,3,y*y + 4) # 3rd arg is rate
      y <- rnorm(1,1/(x + 1),1/sqrt(2*(x + 1)))
    }
    mat[i,] <- c(x,y)
  }
  mat
}

# vals = Rgibbs(10000,500)
# summary(vals)
print(system.time(Rgibbs(10000,500)))