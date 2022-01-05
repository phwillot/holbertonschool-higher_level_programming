#include <Python.h>
/**
 * print_python_list_info - prints info about Python List
 *
 * @p: pointer of PyObject
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %ld: %s\n", i, (PyList_GET_ITEM(p, i)->ob_type->tp_name));
	}
}
