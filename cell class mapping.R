library(png)
library(tidyverse)

# Function to adjust the RGB values based on the alpha channel, assuming a white background
adjust_for_alpha <- function(r, g, b, a) {
  # Normalize alpha and calculate the inverse
  alpha <- a / 255
  inv_alpha <- 1 - alpha
  
  # Adjust each color channel, assuming a white background
  r_adj <- alpha * r + inv_alpha * 255
  g_adj <- alpha * g + inv_alpha * 255
  b_adj <- alpha * b + inv_alpha * 255
  
  return(c(r = r_adj, g = g_adj, b = b_adj))
}

# Read tissue annotation from an image and calculate color ratios
read_tissue_anno <- function(file_name) {
  img <- readPNG(file_name)
  img_dims <- dim(img)
  total_pixels <- img_dims[1] * img_dims[2]
  
  # Check if there is an alpha channel
  if (length(img_dims) == 3 && img_dims[3] == 4) {
    # Apply adjustments for alpha channel
    adjusted_colors <- apply(img, c(1, 2), function(pixel) adjust_for_alpha(pixel[1], pixel[2], pixel[3], pixel[4]))
    img <- abind::abind(adjusted_colors, along = 3)
  }
  
  # Extract RGB values and count colors
  cnt_list <- as.data.frame(table(factor(rgb(img[,,1], img[,,2], img[,,3], maxColorValue = 255), 
                                         levels = rgb(0:255/255, 0:255/255, 0:255/255, maxColorValue = 255))))
  
  names(cnt_list) <- c("color", "count")
  cnt_list$color <- as.character(cnt_list$color)
  cnt_list$class_ratio <- round(cnt_list$count / total_pixels, 3)
  return(cnt_list[c("color", "class_ratio")])
}

# Assign class key based on color
assign_class_key <- function(color) {
  class_mapping <- c(`#a5a5a5` = 'INK', `#a4a4a4` = 'CRSH', `#a2a2a2` = 'OF',
                     `#a0a0a0` = 'AIR', `#9f9f9f` = 'DST', `#9e9e9e` = 'FOLD', `#616161` = 'BG')
  return(ifelse(color %in% names(class_mapping), class_mapping[color], 'ERR'))
}

# Process images in a directory and output results to a CSV file
process_images <- function(input_folder, output_file) {
  file_list <- list.files(input_folder, pattern = "*.png", full.names = TRUE)
  class_keys <- tibble(file_name = character(), class = character(), ratio = numeric())
  
  pb <- txtProgressBar(min = 0, max = length(file_list), style = 3)
  on.exit(close(pb), add = TRUE)  # Ensure progress bar is closed on function exit
  
  for (file in file_list) {
    ratios <- read_tissue_anno(file)
    ratios$class <- sapply(ratios$color, assign_class_key)
    file_name <- tools::file_path_sans_ext(basename(file))
    class_keys <- bind_rows(class_keys, mutate(ratios, file_name = file_name))
    setTxtProgressBar(pb, which(file_list == file))
  }
  
  df_final <- pivot_wider(class_keys, names_from = class, values_from = ratio, values_fill = list(ratio = 0))
  write_csv(df_final, output_file, col_names = TRUE)
}




process_images("file path")