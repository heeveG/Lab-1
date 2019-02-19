#include <stdio.h>


int main(){
    int rows;
    int columns;
    int toprint = 1;
    int counter = 1;
    int firstsymb;
    int secondsymb;
    int thirdsymb;
    printf("Enter rows: ");
    scanf("%i", &rows);
    printf("Enter columns: ");
    scanf("%i", &columns);
    int symbols = columns*rows;

    for(int i = 0; i < symbols+1; i++){
        if(toprint < 10){
            printf("%i", toprint);
            if(counter == symbols){
                break;
            }
            if(counter != 0 && counter % columns == 0){
                printf("\n");
            }
            counter++;

        }else if(toprint < 100){
            firstsymb = toprint / 10;
            secondsymb = toprint % 10;

            printf("%i", firstsymb);
            if(counter == symbols){
                break;
            }
            if(counter % columns == 0){
                printf("\n");
            }

            counter++;

            printf("%i", secondsymb);
            if(counter == symbols){
                break;
            }
            if(counter % columns == 0){
                printf("\n");
            }
            counter++;
        }else{
            firstsymb = toprint / 100;
            secondsymb = toprint % 100 / 10;
            thirdsymb = toprint % 10;

            printf("%i", firstsymb);
            if(counter == symbols){
                break;
            }
            if(counter % columns == 0){
                printf("\n");
            }
            counter++;

            printf("%i", secondsymb);
            if(counter == symbols){
                break;
            }
            if(counter % columns == 0){
                printf("\n");
            }
            counter++;

            printf("%i", thirdsymb);
            if(counter == symbols){
                break;
            }
            if(counter % columns == 0){
                printf("\n");
            }
            counter++;
        }
        toprint++;
    }
}