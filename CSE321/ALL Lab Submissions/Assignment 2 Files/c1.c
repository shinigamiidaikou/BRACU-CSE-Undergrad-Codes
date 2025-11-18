#include <stdio.h>

struct foodItem
{
    int quantity;
    float unit_price;
};

int main()
{
    struct foodItem paratha, vegetable, water;
    int n;
    float total_bill, individual;
    
    printf("Quantity Of Paratha: ");
    scanf("%d", &paratha.quantity);
    printf("Unit Price: ");
    scanf("%f", &paratha.unit_price);

    printf("Quantity Of Vegetables: ");
    scanf("%d", &vegetable.quantity);
    printf("Unit Price: ");
    scanf("%f", &vegetable.unit_price);

    printf("Quantity Of Mineral Water: ");
    scanf("%d", &water.quantity);
    printf("Unit Price: ");
    scanf("%f", &water.unit_price);

    printf("Number of People: ");
    scanf("%d", &n);

    total_bill = (paratha.quantity * paratha.unit_price) +
                 (vegetable.quantity * vegetable.unit_price) +
                 (water.quantity * water.unit_price);

    individual = total_bill / n;

    printf("Individual people will pay: %.2f tk\n", individual);

    return 0;
}
