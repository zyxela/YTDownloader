package com.example.youtubedownloader

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.chaquo.python.PyObject
import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking

class MainViewModel : ViewModel() {
    val currentProgress: MutableLiveData<Int> by lazy {
        MutableLiveData<Int>()
    }

    init {
        currentProgress.value = 0
    }

    fun updateProgress(module: PyObject) = runBlocking {
        val downloader = module["downloader"]

        while (true) {
            currentProgress.postValue(downloader?.callAttr("return_progress_statement")?.toInt())
            delay(10)
        }

    }


}