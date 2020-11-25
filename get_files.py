import os
import shutil

def get_files(top, include=None, exclude=None):
    """Get all fullpath files in top directory"""
    if not top:
        raise ValueError('Top must be not null')
    
    results = []
    for root, dirs, files in os.walk(top):
        for f in files:
            if include:
                if f in include:
                    results.append(os.path.join(root, f))
            else:
                results.append(os.path.join(root, f))
    return results

def copy_files(files, dst):
    """Copy files to dst folder"""
    if not dst:
        raise ValueError('Dst folder must be not null')
    for f in files:
        print(dst, os.path.join(dst, f))
        os.makedirs(os.path.join(dst, f))

if __name__ == "__main__":
    top_path = '/media/leloc/Learning/08_python/50_project/fastvoca'
    copy_dst = os.path.join(top_path, 'perf')

    if not os.path.isdir(copy_dst):
        os.mkdir(copy_dst)

    files = get_files(top_path, include=['models.py'])
    copy_files(files, copy_dst)