package com.example.youtubedownloader

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class MainViewModel : ViewModel() {

    val currentProcess: MutableLiveData<Int> by lazy {
        MutableLiveData<Int>()
    }

    init {
        currentProcess.value = 0
    }


}