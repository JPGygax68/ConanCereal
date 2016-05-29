#include <sstream>
#include <iostream>

#include <cereal/types/string.hpp>
#include <cereal/archives/binary.hpp>

int main(int argc, char *argv[])
{
    std::string in_string = "Hello World!";
    std::stringstream sstream;
    cereal::BinaryOutputArchive ar_out{ sstream };
    ar_out(in_string);

    cereal::BinaryInputArchive ar_in{ sstream };
    std::string out_string;
    ar_in(out_string);

    std::cout << out_string << std::endl;

    return 0;
}