#include <stdio.h>
#include <opencv2/opencv.hpp>

int 
main (int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("usage: DisplayImage.out <Image_Path>\n");
        return -1;
    }

    printf("argv = %p\n", argv);
    printf("*argv = %p\n", *argv);
    printf("*(argv + 1) = %p\n", *(argv + 1));
    
    char* ch = *(argv + 1);
    while (*ch != '\0')
    {
      printf("%c", *ch);
      ch += 1;
    }
    printf("\n");

    cv::Mat image;

    image = cv::imread( *(argv + 1), 1 );

    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }

    cv::namedWindow("Display Image", cv::WINDOW_AUTOSIZE );
    cv::imshow("Display Image", image);
    cv::waitKey(0);

    return 0;
}
