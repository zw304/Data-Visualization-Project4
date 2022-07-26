library(plotly)
library(plyr)

data<- read.csv("data_munging.csv")

head(data)
data$Date<-as.character(data$Date) ## change data type of the Date column 
str(data)

## question: among working_usage(lamp,laptop,router),entertainment, daily_usage(coffee,frigde,kettle), which one and which subcategory has the most usage?

fig1 <- plot_ly(alpha = 0.7) %>% 
  add_histogram(x = ~data$Lamp,
                name = "Lamp") %>% 
  add_histogram(x = ~data$Laptop,
                name = "Laptop & Printer") %>% 
  add_histogram(x = ~data$Router,
                name = "Router & sheeva plug computer")%>%
  layout(barmode = "overlay",
       xaxis = list(title = "Working Usage(in 10 Watts)",
                    zeroline = FALSE))

  fig2<-plot_ly(alpha = 0.7) %>%
  add_histogram(x = ~data$Entertainment,
                name = "Entertainment (TV & stereo)") %>%
    layout(barmode = "overlay",
           xaxis = list(title = "Entertainment Usage(in 10 Watts)",
                        zeroline = FALSE))
  
  fig3<-plot_ly(alpha = 0.7) %>%
  add_histogram(x = ~data$Coffee,
                name = "Coffee") %>% 
  add_histogram(x = ~data$Fridge,
                name = "Fridge") %>%
  add_histogram(x = ~data$Kettle,
                name = "Kettle") %>%
    layout(barmode = "overlay",
           xaxis = list(title = "Daily common Usage(in 10 Watts)",
                        zeroline = FALSE))
  
  fig<-subplot(fig1,fig2,fig3,shareY = TRUE, titleX = TRUE)%>%
  layout(barmode = "overlay",
         title = "Histogram for Power Coverage in different Categories",
         yaxis = list(title = "Power Usage Frequency",
                      zeroline = FALSE))
fig
