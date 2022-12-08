#include <stdio.h>
#include <pthread.h>

pthread_mutex_t S1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t S2 = PTHREAD_MUTEX_INITIALIZER;

void *driver_process(void *arg)
{
    while (1)
    {
        pthread_mutex_lock(&S1);  // 等待售票员发送关门信息
        printf("启动车辆...\n");
        printf("正常行车...\n");
        printf("到站停车...\n");
        pthread_mutex_unlock(&S2);  // 给售票员发送到站信息
    }
}

void *ticket_seller_process(void *arg)
{
    while (1)
    {
        printf("关车门...\n");
        pthread_mutex_unlock(&S1);  // 给司机发送关门信息
        printf("售票...\n");
        pthread_mutex_lock(&S2);  // 等待司机发送到站信息
        printf("开车门...\n");
        printf("上下乘客...\n");
    }
}

int main()
{
    pthread_t driver, ticket_seller;
    pthread_create(&driver, NULL, driver_process, NULL);
    pthread_create(&ticket_seller, NULL, ticket_seller_process, NULL);
    pthread_join(driver, NULL);
    pthread_join(ticket_seller, NULL);
    return 0;
}
