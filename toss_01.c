#include <stdio.h>
#include <stdlib.h>
#include <math.h>


long long	solution(long long orderAmount, long long taxFreeAmount, long long serviceFee)
{
	// orderAmount : 주문금액
    	// taxFreeAmount : 비과세금액(부가 가치세가 부과되지 않는 금액)
    	// serviceFee : 봉사료
    	long long	answer = 0;
	long long	amount_of_value = 0;

	amount_of_value = orderAmount - serviceFee;
	if (amount_of_value - taxFreeAmount == 1)
		return (answer);
	answer = ceill((((long double) amount_of_value - (long double)taxFreeAmount) / 11));
	return (answer);
}

int	main(void)
{
	printf("[%lld]\n", solution(120, 20, 0));
	printf("[%lld]\n", solution(100, 0, 0));
	printf("[%lld]\n", solution(120, 0, 20));
	return (0);
}
