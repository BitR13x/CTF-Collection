// init of free_space
free_space = (long *)malloc(0x30000); // int 196608
*free_space = 1;

// I will get pointer to free_space
printf("%p",free_space);

// segmentation on long int
scanf("%lu",&input_int);

n_size_malloc = malloc(input_int);
  // stdin, write, n_bytes
read(0, n_size_malloc, input_int);



//! I need: 
// a + (b - 1) = free_space

n_size_malloc + (input_int - 1) = 0;


// I need:
if (*free_space == 0) {
  read_flag();
}