import pk3hunum
print pk3hunum.hunum({
    'total': 10240,
    'progress': [1, 1024*2.1, 1024*3.2],
})
# {"total" : "10K", "progress" : [1, "2.1K", "3.2K"]}
