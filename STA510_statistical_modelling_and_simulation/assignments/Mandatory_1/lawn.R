rm(list=ls())
sim.lawn<-function(Etime=10.0,plot.trace=FALSE,plot.image=FALSE){
  rbound <- 20
  ubound <- 30
  
  Tmax <- 1500 # seconds
  sampleRate <- 10 # discrete samples per second
  events <- matrix(0.0,round(100/min(10,Etime)*Tmax),3)
  events[1,] <- c(0,0,0.5*ubound)
  samples <- matrix(0.0,Tmax*sampleRate,2)
  
  eventCount <- 1
  sampleCount <- 0
  
  time <- 0.0
  v <- c(1,2)
  v <- v/sqrt(sum(v^2)) #c(1.0,0.0)
  
  while(time < Tmax){
    nextTime <- time + Etime*(-log(runif(1))) # random time
    vnew <- rnorm(2)
    vnew <- vnew/sqrt(sum(vnew^2))
    if(v[1]>0.0){
      # hits right boundary
      collisionTime <- time + (rbound-events[eventCount,2])/v[1]
      if(collisionTime<nextTime){
        nextTime <- collisionTime
        vnew <- c(-v[1],v[2])
      }
    } else if(v[1]<0.0) {
      # hits left boundary
      collisionTime <- time + (-events[eventCount,2]/v[1])
      if(collisionTime<nextTime){
        nextTime <- collisionTime
        vnew <- c(-v[1],v[2])
      }
    }
    if(v[2]>0.0){
      #hits upper boundary
      collisionTime <- time + (ubound-events[eventCount,3])/v[2]
      if(collisionTime<nextTime){
        nextTime <- collisionTime
        vnew <- c(v[1],-v[2])
      }
    } else if(v[2]<0.0){
      #hits lower boundary
      collisionTime <- time + (-events[eventCount,3])/v[2]
      if(collisionTime<nextTime){
        nextTime <- collisionTime
        vnew <- c(v[1],-v[2])
      }
    }
    nextTime <- min(nextTime,Tmax)
    eventCount <- eventCount+1
    events[eventCount,1] <- nextTime
    events[eventCount,2:3] <- events[eventCount-1,2:3] + (nextTime-time)*v
    
    lastSample <- floor(nextTime*sampleRate)
    if(lastSample>sampleCount){
      tgrid <- (1.0/sampleRate)*((sampleCount+1):lastSample)
      samples[(sampleCount+1):lastSample,1] <- events[eventCount-1,2] + (tgrid-time)*v[1]
      samples[(sampleCount+1):lastSample,2] <- events[eventCount-1,3] + (tgrid-time)*v[2]
      sampleCount <- lastSample
    }
    v <- vnew
    time <- nextTime
  }
  
  
  
  if(plot.trace && plot.image){
    par(mfrow=c(1,2))
  } else if(plot.trace || plot.image) {
    par(mfrow=c(1,1))
  }
  if(plot.trace) {
    par(bg = "green")
    events <- events[1:eventCount,]
    plot(events[,2],events[,3],"l",xlab="x",ylab="y",main="trace of lawn mower")
  }
  gret <- gplots::hist2d(rbind(events[1,2:3],c(0,0),c(rbound,ubound),samples),nbins=c(5*rbound,5*ubound),show=FALSE)
  
  if(plot.image) image(x=gret$x,y=gret$y,z=gret$counts>0,xlab="x",ylab="y",main="grid cells visited")
  
  return(sum(gret$counts>0)/prod(dim(gret$counts)))
}

if(F){
set.seed(1)
nrep <- 100
mat <- matrix(0.0,nrep,4)
for(i in 1:nrep){
  mat[i,1] <- simulate.lawn(Etime=1.0)
  mat[i,2] <- simulate.lawn(Etime=10.0)
  mat[i,3] <- simulate.lawn(Etime=100.0)
  mat[i,4] <- simulate.lawn(Etime=1000.0)
}
res.df <- data.frame(mat)
colnames(res.df) <- c("Etime=1","Etime=10","Etime=100","Etime=1000")
}




