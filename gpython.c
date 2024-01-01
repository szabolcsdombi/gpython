#include <Python.h>

extern _declspec(dllexport) int NvOptimusEnablement = 0x00000001;
extern _declspec(dllexport) int AmdPowerXpressRequestHighPerformance = 0x00000001;

#ifdef MS_WINDOWS
int
wmain(int argc, wchar_t **argv)
{
    return Py_Main(argc, argv);
}
#else
int
main(int argc, char **argv)
{
    return Py_BytesMain(argc, argv);
}
#endif
