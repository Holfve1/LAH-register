import '@testing-library/jest-dom'
import { afterEach, beforeAll, vi } from 'vitest'
import { cleanup } from '@testing-library/react'

beforeAll(() => {
  if (!global.fetch) {
    global.fetch = vi.fn()
  }
})
afterEach(() => {
  cleanup()
  vi.clearAllMocks()
  localStorage.clear()
})