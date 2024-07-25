bool isPalindrome(int x)
{
    int temp=x;
    double sum=0;
    while(temp!=0)
    {
        int y=temp%10;
        sum=sum*10+y;
        temp=temp/10;
    }
    if(sum==x)
    {
        if(x<0)
        return 0;
        else
        return 1;
    }
    else
    return 0;
}