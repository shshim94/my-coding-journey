library(magick)
library(tidyverse)
library(progress)

# Function to assign class key
assign_class_key <- function(r, g, b) {
  class_mapping <- list(
    'c(165, 165, 165)' = 'INK',
    'c(164, 164, 164)' = 'CRSH',
    'c(162, 162, 162)' = 'OF',
    'c(160, 160, 160)' = 'AIR',
    'c(159, 159, 159)' = 'DST',
    'c(158, 158, 158)' = 'FOLD',
    'c(97, 97, 97)' = 'BG'
  )
  
  key <- paste(r, g, b, sep = ", ")
  return(ifelse(key %in% names(class_mapping), class_mapping[[key]], 'ERR'))
}

# Function to process images in a directory
process_images <- function(input_folder, output_file) {
  files <- list.files(path = input_folder, pattern = "*.png", full.names = TRUE)
  results <- tibble()
  pb <- progress_bar$new(total = length(files), format = "  [:bar] :percent :elapsedfull", clear = FALSE, width = 60)
  
  for (file in files) {
    file_name <- tools::file_path_sans_ext(basename(file))
    image <- image_read(file) %>%
      image_convert(colorspace = 'sRGB')  # Convert to sRGB to remove alpha channel
    
    # Convert image to array and then to a data frame
    color_data <- as.integer(image_data(image, channels = "RGB"))
    colors <- data.frame(r = color_data[1, ,1], g = color_data[1,,2], b = color_data[1,,3])
    
    # Calculate class ratios
    count_colors <- colors %>%
      group_by(r, g, b) %>%
      summarise(n = n(), .groups = 'drop') %>%
      mutate(class_ratio = round(n / sum(n), 3),
             key = mapply(assign_class_key, r, g, b))
    
    # Flatten and include the file name
    count_colors <- count_colors %>% mutate(file_name = file_name)
    results <- bind_rows(results, count_colors)
    
    pb$tick()  # Update the progress bar
  }
  
  write.csv(results, file = output_file, row.names = FALSE)
}

# Example usage
input_folder <- "file path"  # Update the path if needed
output_file <- "output file name"
process_images(input_folder, output_file)
