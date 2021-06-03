#ifdef MYDLL_EXPORTS
#define MYDLL_API __declspec(dllexport) 
#else
#define MYDLL_API __declspec(dllimport) 
#endif



extern "C" MYDLL_API int Hour();

extern "C"  MYDLL_API int Minute();

extern "C"  MYDLL_API int Second();

