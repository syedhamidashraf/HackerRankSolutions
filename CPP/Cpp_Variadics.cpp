

// Enter your code for reversed_binary_value<bool...>()
template <typename = void>
int reversed_binary_value()
 {
     return 0;
 }

template <bool a, bool... b>
int reversed_binary_value()
{
    return (reversed_binary_value<b...>() <<1)+a;
}
